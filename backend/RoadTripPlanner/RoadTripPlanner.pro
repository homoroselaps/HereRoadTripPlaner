TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

include(deployment.pri)
qtcAddDeployment()

INCLUDEPATH += \
    source \
    source/fossa

SOURCES += \
    source/main.cpp \
    source/fossa/fossa.c

HEADERS += \
    source/fossa/fossa.h

