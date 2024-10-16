# Instructions for stage-lights

## On the Raspberry Pi

```bash
cd
rm -rf stage-lights
git clone https://github.com/3lv/stage-lights
bash stage-lights/install.sh
```
In the menu:
- Enable VNC(Interface options > VNC > Yes)
- Make sure Desktop is enabled (System Options > Boot / Auto Login > Desktop Autologin)


## On the iPad mini

1. From the App Store, install `RealVNC Viewer`

2. Login to your Raspberry Pi (find it's ip on the local network)

3. In the terminal, launch the gui app:

```bash
python3 stage-lights/gui.py
```

4. Should be working!!

## Aditional info

- Ensure the Raspberry Pi is properly powered, as activating multiple relays simultaneously could cause it to CRASH.
