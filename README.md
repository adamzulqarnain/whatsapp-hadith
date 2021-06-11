# whatsapp-hadith
Python script to send hadith to selected contacts/group via WhatsApp using selenium, requests and json libs

## Basic Information:
1. All hadiths used are being fetched from this API: https://api.sunnah.com/v1/hadiths/random
2. In order to request via API, you would need to include x-api-key in the headers specified in `configuration/config.py`. You can request for API access here https://github.com/sunnah-com/api/issues

## Shortcuts:
1. [Tools/API Used](#toolsapi-used)
2. [Host Configuration](#host-configuration)
3. [Setting Up](#setting-up)
4. [Managing Contacts](#managing-contacts)
5. [WhatsApp Message Format](#whatsapp-message-format)
6. [Limitations](#limitations)
7. [TODO](#todo)

## Tools/API Used:
1. **python**
2. **selenium** webdriver API
3. **request** lib for REST request
4. **json** lib to read REST response
5. **re** lib to use regex for striping HTML code in response body

## Host Configuration:
1. **HW**: Raspberry Pi 4 Model B Rev 1.2
2. **OS**: Raspbian GNU/Linux 10 (buster)
3. **Kernel**: 5.4.51-v7l+

## Setting Up:
1. Create venv and install dependencies specified in requirements.txt
   ```
   pip install -r requirements.txt
   ```
2. Due to some limitation, chromium on raspbian doesnt allow whatsapp web hence a workaround is needed. Full context and information available [here](https://blog.vpetkov.net/2019/07/12/netflix-and-spotify-on-a-raspberry-pi-4-with-latest-default-chromium/)
   or TLDR version, run the following commands on raspberry pi terminal
   ```
   sudo su
   cd /usr/lib/chromium-browser
   wget http://blog.vpetkov.net/wp-content/uploads/2020/03/libwidevinecdm.so_.zip
   unzip libwidevinecdm.so_.zip && chmod 755 libwidevinecdm.so
   wget http://blog.vpetkov.net/wp-content/uploads/2020/03/chromium-media-browser.desktop.zip
   unzip chromium-media-browser.desktop.zip && mv chromium-media-browser.desktop /usr/share/applications
   ```
3. Run following script to open chromium browser using a specific port, in this case port: 9999
   ```
   setup_raspberry.sh
   ```
4. Once browser is up and running, you need to navigate to `web.whatsapp.com` and scan QR code using your phone (only needed once). Note that you cannot close this browser as the script will always use this browser to send whatsapp messages

5. Setup crontab to schedule when to send out these messages, frequency of sending depends on the configuration you set on crontab. In this case, I used the following config which will send the messages at 9am everyday
   ```
   0 9 * * * /home/pi/repo/whatsapp-hadith/run.sh
   ```
 
## Managing Contacts:
1. Edit the following variable inside `configuration/contacts.py` to add contacts (needs to be in string format) you want to send messages to:
   ```
   contacts = ["Manjung Tribes", .., ..]
   ```

## WhatsApp Message Format:
![ws](https://i.imgur.com/QAj2suM.png)
   
## Limitations:
1. Group names need to be unique, otherwise message may be sent to unintended group

## TODO: 
1. Add support to get argument parameter to handle setup on linux or windows as well
2. Add support for firefox (geckodriver)
3. Add exception handling when running script to handle any erros
4. Add logging/print traces for debugging purposes
