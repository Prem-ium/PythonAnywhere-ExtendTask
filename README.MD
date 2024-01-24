<h1 align="center">📊 PythonAnywhere Task Extension Automation 🤖 </h1>

<p align="center">A very simple Selenium script to extend tasks on PythonAnywhere.</p>

<p align="right"> 
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><a href="https://www.buymeacoffee.com/prem.ium" target="_blank"><img align="right" src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee"/></a><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a>
</p>

## Installation
Clone the repository & Install dependencies
```bash
  git clone https://github.com/Prem-ium/PythonAnywhere-ExtendTask.git
  cd PythonAnywhere-ExtendTask
  pip install -r requirements.txt
```
Finally, you're ready to run the script!
```bash
  python main.py
```
## Enviornmental Variables
- `LOGIN` - USERNAME:PASSWORD. PythonAnywhere login, seperated by ':'

# Scheduling Python Script Weekly on Windows and Linux Startup
## Windows

To schedule the execution of a Python script on Windows every week when the system boots, you can use the Task Scheduler. Follow these steps:

1. **Open Task Scheduler:** Press `Win + S`, type "Task Scheduler," and select it from the search results.

2. **Create a Basic Task:**
   - Click on "Create Basic Task" in the right-hand menu.
   - Follow the wizard to set a name and description for your task.

3. **Trigger Settings:**
   - Choose the "Weekly" trigger option.
   - Set the day and time you want the script to run each week.

4. **Action Settings:**
   - Select "Start a program" as the action.
   - Browse and select the Python executable (e.g., `python.exe`) as the program/script.
   - In the "Add arguments" field, provide the path to your Python script (e.g., `C:\path\to\your\script.py`).

5. **Finish:**
   - Review your settings and complete the wizard.

Your Python script will now run every week at the specified day and time when the Windows system starts.

## Linux

To schedule the execution of a Python script on Linux every week during boot, you can use `cron`. Follow these steps:

1. **Open the Crontab Editor:**
   - Open a terminal.
   - Type `crontab -e` to edit the crontab file.

2. **Add a Weekly Cron Job:**
   - In the editor, add the following line to run your Python script every week at boot:
     ```
     @reboot /path/to/python3 /path/to/your/script.py
     ```
     Replace `/path/to/python3` with the path to your Python interpreter (use `which python3` to find it) and `/path/to/your/script.py` with the path to your Python script.

3. **Save and Exit:**
   - Save the changes and exit the crontab editor.

Now, your Python script will be executed every week when the Linux system boots up.

Note: Ensure that your Python script has the necessary permissions to run and that any required dependencies are available.

## Donations
1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - This is the preferred donation method as you can place donations with no transaction fees & possibily receive perks for your donation.
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

## License
This repository is using the [MIT](https://choosealicense.com/licenses/mit/) license.
