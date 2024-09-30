Automated Voting Bot for Captcha-Based Games
This project automates the voting process in an online game that uses a poorly secured CAPTCHA system. The Python script opens a Chrome browser tab, navigates to the voting website, scrapes the CAPTCHA images, and stores them in numbered folders (1-9).

The bot then compares the scraped images with those stored in the folders. If a match is found, the bot correctly answers the CAPTCHA.

This method is effective because the CAPTCHA system uses the same images repeatedly, only updating them every few weeks. By storing these images, the bot is able to automate the voting process over time as it builds a complete dataset of CAPTCHA images.
