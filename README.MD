# 📊 PythonAnywhere Task Extension Automation 🤖

<p align="center">A <i>simple</i> Selenium script to extend tasks across multiple PythonAnywhere accounts.</p>

<p align="right">  
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>  
    <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>  
    <a href="https://github.com/sponsors/Prem-ium" target="_blank">  
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="GitHub Sponsor"/>  
    </a>  
</p>  

---
## 🚀 Installation
Clone the repository and install dependencies:
```bash
  git clone https://github.com/Prem-ium/PythonAnywhere-ExtendTask.git
  cd PythonAnywhere-ExtendTask
  pip install -r requirements.txt
```
Run the script:
```bash
  python main.py
```

---
## 🔧 Environment Variables

- **`LOGIN`**: A comma-separated string of PythonAnywhere credentials, where each credential consists of a username and password separated by a colon (`:`).  
  **Example:**  
  ```plaintext
  LOGIN="USERNAME:PASSWORD,USERNAME2:PASSWORD2,ACCOUNT3:PASSWORD3"
  ```

---
## ⏳ Scheduling the Script

### 🖥️ Windows (Task Scheduler)
1. Open **Task Scheduler** (`Win + S`, search "Task Scheduler").
2. Click **Create Basic Task** and set a name/description.
3. Select **Weekly** trigger and choose a time.
4. Choose **Start a program**, browse to `python.exe`, and add the script path in **arguments**.
5. Finish setup – the script will now run weekly at the specified time.

### 🐧 Linux (Cron Job)
1. Open a terminal and edit crontab:
   ```bash
   crontab -e
   ```
2. Add this line to run the script at startup:
   ```bash
   @reboot /path/to/python3 /path/to/your/script.py
   ```
3. Save and exit – the script will now execute on every system boot.

*Ensure the script has execution permissions and dependencies installed.*

---
## 💖 Support & Donations
### 1️⃣ GitHub Sponsors
- [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium) *(Preferred: No transaction fees + perks!)*  
  [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

### 2️⃣ Buy Me A Coffee
- [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)  
  [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

### 3️⃣ Referral Links (Free Support)
- Use my curated [Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md) to earn bonuses and support my projects at no cost!  
  [Explore Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md)

---
## 📜 License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.