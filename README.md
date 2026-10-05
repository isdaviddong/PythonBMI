# BMI 計算器

使用 Flask 製作的成人 BMI 網頁計算器。輸入身高（公分）和體重（公斤）後，頁面會顯示 BMI（小數點後一位）、體位分類與生活建議。

## 啟動

需安裝 Python 3.9 以上版本。在專案資料夾執行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

接著開啟 http://127.0.0.1:5000/ 。若 PowerShell 不允許啟用虛擬環境，也可以使用 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` 和 `.\.venv\Scripts\python.exe app.py`。

## 計算方式

BMI = 體重（公斤）÷ 身高（公尺）²。分類採臺灣成人體位參考標準：低於 18.5 為體重過輕、18.5 至未滿 24 為健康體位、24 至未滿 27 為體重過重、27 以上為肥胖。頁面以顯示至小數點後一位的 BMI 進行分類。

這只是成人體位參考，不能取代專業醫療評估，也不適用於兒童、青少年或孕婦。

執行測試：`python -m unittest discover -s tests`

## 部署到 Azure Web App

`.github/workflows/deploy-azure.yml` 在 `main` 分支的應用程式、測試或 workflow 異動時執行，也可以從 GitHub Actions 手動觸發。流程會先執行測試，再透過 Azure App Service 的建置自動化安裝 `requirements.txt`，以 Gunicorn 啟動 Flask。

部署前請準備 **Linux** Azure Web App，並使用 **Python 3.12** 執行環境。Azure App Service 不再支援在 Windows Web App 上直接執行 Python；現有的 `NTUSTweb00` 是 Windows Web App，不能作為此流程的部署目標。

在 GitHub 儲存庫 **Settings → Secrets and variables → Actions** 設定：

- Repository secret `AZURE_CREDENTIALS`：Azure 服務主體的 `clientId`、`clientSecret`、`subscriptionId`、`tenantId` 組成的 JSON。此 Secret 已設定，不要把內容寫進程式碼。
- Repository variable `AZURE_WEBAPP_NAME`：新 Linux Web App 的名稱。
- Repository variable `AZURE_RESOURCE_GROUP`：該 Web App 所在資源群組。

請確認該服務主體對新的 Linux Web App 具有部署及更新應用程式設定的權限（例如該站點的 **Website Contributor**）。設定完成後，可由 GitHub Actions 手動執行一次工作流程，或推送符合上述條件的 `main` 分支異動。未填變數或目標不是 Linux Web App 時，流程會在部署前明確失敗。
