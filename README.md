# bitmessage-answeringmachine
## Description
A text based answering machine script for BitMessage. Use it to send away messages to clients, friends, co-workers or whomever your communicating with; furthermore, the messages you receive are save so you can answer their messages at a later date.

## Features
* Write custom away message
* Saves messages locally 
* Deletes messages from BitMessage 

## System Requirements
* Python 2.7.x 
* BitMessage 0.4.4

## Installation Instructions
1. Install PyBitmessage and run it once. Close BitMessage.

2. Look for the keys.dat file on your OS. The first time it runs it will create this.
  * Linux: ~/.config/PyBitmessage/keys.dat
  * Windows: TBD
  * OSX: ~/Library/Application\ Support/PyBitMessage/keys.dat

3. Once you find this file, open it, and under the [bitmessagesettings] heading put in the following options:
  ```
  apienabled = true
  apiport = 8442
  apiinterface = 127.0.0.1
  apiusername = username
  apipassword = password
  ```

4. Start up BitMessage again.

5. Open “answeringmachine.py” file and make sure you add your BitMessage address and the location of the BitMessage Server running.

6. Open “outbox_tape” and modify it to whatever message you want. 

7. Run the script from console by entering
  ```bash
  # python2.7 answeringmachine.py
  ```

8. Create a cronjob in your environment to call this script periodically. Now whenever someone sends you a message to your address, the sender’s message will get saved and s/he will receive an away message from you.

## Usage
Simply running this script every time you want your BitMessage inbox to by processed by the answering machine.
```bash
# python2.7 answeringmachine.py
```
## License
MIT

## Comments
While this may seem like a boring answering machine, there are a few cool things you can do with it:

1. You can have servers override the “outbox_tape.txt” contents with logs or any specific messages you want.

2. You can purchase digital sensors (Ex. Thermometer), write a script to overriding “outbox_tape.txt” contents with specific environmental/sensory data.

3. You can write news story or keep tallied data to share anonymously with your followers.

## Donate
* Bitcoin: 17VEy2fps6nJCUhWsvhJ4h42omWMJZUjcm
* Darkcoin: XmrxCpPD8xCFgoVjR7eqqdzrXiy9rWedv7
