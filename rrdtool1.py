import rrdtool
def grafica1():
    ret = rrdtool.create("bdrrdtool/g1.rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())


def grafica2():
    ret = rrdtool.create("bdrrdtool/g2.rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())


def grafica3():
    ret = rrdtool.create("bdrrdtool/g3.rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())


def grafica4():
    ret = rrdtool.create("bdrrdtool/g4.rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())


def grafica5():
    ret = rrdtool.create("bdrrdtool/g5.rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())

