# Manyloris
**_Run Slowloris against multiple targets_**

> Slowloris is a type of denial of service attack tool which allows a single machine to take down another machine's web server with minimal bandwidth and side effects on unrelated services and ports.

Check out the original tool here:
https://github.com/gkbrk/slowloris

### Manyloris
Manyloris is a tool that allows to run Slowloris for multiple targets. It receives a list of targets and ports.

#### Usage:
-> You must have Slowloris installed before trying to run Maniloris.
`python3 maniloris [TARGET_LIST]`
**NOTE: The target list must have each IP on a new line and have the following syntax -> IP:PORT:PORT:PORT:...**
