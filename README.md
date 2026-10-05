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
