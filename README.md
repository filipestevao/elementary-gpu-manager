# Elementary GPU Manager

Utility for managing graphics and power profiles in ElementaryOS.

## Description

Graphical user interface to easily switch between Intel/Nvidia GPU.

**Motivation:** I like Elementary OS, its interface and philosophy. However, I have a hybrid-graphic notebook, which made it difficult to use the operating system. So I decided to install the [system76-power](https://support.system76.com/articles/graphics-switch-ubuntu/) of [System76](https://system76.com/), adding the PPA. This process worked at ElementaryOS; however, requiring the terminal at all times is laborious, so I decided to create a graphical interface to make things easier.

*Figure here*

## Instalation

1. First, make sure your system is up to date.
1. [Download this repository](https://github.com/filipestevao/elementary-gpu-manager/archive/master.zip).
1. Run `install.sh`:

```
sh ./install.sh
```
This should install `system76-power` and the graphical interface.

## Notes

### Graphics card information

To view the graphics card information:

```
glxinfo | grep OpenGL
```

### Testing FPS

To test the FPS (*Nvidia's FPS should be higher*):

```
__GL_SYNC_TO_VBLANK=0 glxgears
```

### Kernel updates

After each kernel update, the following command will be required:

```
sudo dpkg --configure -a
```

To be sure that you must run this command, just run `sudo apt update && sudo apt upgrade` and a warning should appear.