# How to run this sample
- Since the latest release of Miniconda in this moment is attached to Python 3.8 and fbprophet needs Python 3.6 you will need to download any of these Windows Versions:
  - Miniconda3-4.5.4-Windows-x86.exe
  - Miniconda3-4.5.4-Windows-x86_64.exe

  > Reference: https://repo.anaconda.com/miniconda/ 

- Once you downloaded, zip all content of the installation and create a new folder in KUDU Site `https://<sitename>.scm.azurewebsites.net/DebugConsole` under `D:\home\site` called `miniconda3`
- Since this sample is using custom deployment script, the script has two phases, one installing all requirements.txt with libraries needed, and then installing just fbprophet as followed:
   - D:\home\site\miniconda3\Scripts\conda.exe install --yes --file requirements.txt
   - D:\home\site\miniconda3\Scripts\conda.exe install --yes -c conda-forge fbprophet
- This deployment process can take more than 15 mins. You will need to increase this parameter
`SCM_COMMAND_IDLE_TIMEOUT` `https://github.com/projectkudu/kudu/wiki/Configurable-settings#changing-the-timeout-before-external-commands-are-killed`