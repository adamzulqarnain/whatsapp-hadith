# whatsapp-hadith
Python script to send hadith to selected contacts/group via WhatsApp using selenium, requests and json libs

> A hadith a day, keeps our iman at bay. InsyaAllah :)

## Tools/API used:
1. **python**
2. **selenium** webdriver API
3. **request lib** for REST request
4. **json** lib to read REST response
5. **re** lib to use regex for striping HTML code in response body

## My configuration:
1. Model: Raspberry Pi 4 Model B Rev 1.2
2. OS: Raspbian GNU/Linux 10 (buster)
3. Kernel: 5.4.51-v7l+

## Setting up:
1. Create venv and install dependencies on requirements.txt
   ```
   pip install -r requirements.txt
   ```
2. Due to some limitation, chromium on raspbian doesnt allow whatsapp web hence a workaround is needed. Full context and information available [here](https://blog.vpetkov.net/2019/07/12/netflix-and-spotify-on-a-raspberry-pi-4-with-latest-default-chromium/)
   or TLDR version, run the follow command on raspberry pi terminal
   ```
   # sudo su
   # cd /usr/lib/chromium-browser
   # wget http://blog.vpetkov.net/wp-content/uploads/2020/03/libwidevinecdm.so_.zip
   # unzip libwidevinecdm.so_.zip && chmod 755 libwidevinecdm.so
   # wget http://blog.vpetkov.net/wp-content/uploads/2020/03/chromium-media-browser.desktop.zip
   # unzip chromium-media-browser.desktop.zip && mv chromium-media-browser.desktop /usr/share/applications
   ````
3. Run following script to open chromium browser using a specific port, in this case port: 9999
   ```
   setup_raspberry.sh
   ```
4. Once browser is up and running, you need to navigate to web.whatsapp.com and scan QR code from your phone (only needed once). Note that you cannot close this browser as the script will always use this browser to send whatsapp messages
5. Setup crontab to schedule when to send out these messages, frequency of sending depends on the configuration you set on crontab. In this case, I used the following config which will send the messages at 9am everyday
   ```
   0 9 * * * /home/pi/repo/whatsapp-hadith/run.sh
   ```
 
## Managing contacts
1. Edit the following variable inside `config.py` to add contacts (needs to be in string format) you want to send messages to:
   ```
   contacts = ["Manjung Tribes", .., ..]
   ```

// TODO: 
1. Add support to get argument parameter to handle setup on linux or windows as well
2. Get a dedicated phone number and phone, any interested group and add this number into their group. Once configured, hadith will be send to these whatsapp group on a daily basis
