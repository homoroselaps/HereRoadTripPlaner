TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += source/main.cpp \
    source/fossa/fossa.c

include(deployment.pri)
qtcAddDeployment()

HEADERS += \
    source/fossa/fossa.h

