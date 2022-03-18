# Manyloris 🇺🇦
**Run Slowloris against multiple targets.**

> Slowloris is a type of denial of service attack tool which allows a single machine to take down another machine's web server with minimal bandwidth and side effects on unrelated services and ports.

Check out the original tool here:
https://github.com/gkbrk/slowloris.

### Manyloris
Manyloris is a tool that allows to run Slowloris for multiple targets. It receives a list of targets and ports.

#### Usage:
-> You must have Slowloris installed before trying to run Manyloris.

`python3 manyloris [TARGET_LIST]`

**NOTE: The target list must have a target IP per line and follow the syntax** "IP:PORT:PORT:PORT:..."

```Example list:
123.423.1.1:80:443
12.1.612.123:80:443:8443
231.23.522.3:443:80
141.101.123.30:443
```
#### To improve:
* Allow stopping the Slowloris processes with a POSIX signal.
* Support the input of additional arguments.
* Allow running for a signle target, as well.
* Have more checks and better deal with exceptions.
* Allow passing targets in different ways, other than a list.
* Validate the passed list.
* Automatically cleaning a list through regex.
