#ifndef SERIALPORT_H_
#define SERIALPORT_H_

#include
#include
#include
#include

class SerialPort {
private:
    int fileDescriptor;
    
public:
    int connect ();
    int connect (char * device);
    void disconnect(void);
    
    int sendArray(unsigned char *buffer, int len);
    int getArray (unsigned char *buffer, int len);
    
    int bytesToRead();
    void clear();
};

#endif /* SERIALPORT_H_ */
