## About
A simple script, get inspired when using your terminal.

## Installing
Simply fire up your terminal and run the installation script to install it on your system.
```bash 
git clone https://gitlab.com/vedantnn7/quoty.git
cd quoty
./install
```

### Manual inspection
1. Fire up your terminal emulator and clone this repo.
   ```bash
   git clone https://gitlab.com/vedantnn7/quoty.git
   ```
2. Cd into the quoty directory and copy quoty file to ~/.local/bin/
   ```bash
   cd quoty
   cp ./quoty ~/.local/bin
   ```
3. Run the following command to get quotes when you run your terminal emulator.
   If you're using bash - 
   ```bash
   echo 'quoty' >> ~/.bashrc
   ```
   If you're using zsh -
   ```zsh
   echo 'quoty' >> ~/.zshrc
   ```
That's it! Pull requests are welcome, open a request if you encounter any problem.
