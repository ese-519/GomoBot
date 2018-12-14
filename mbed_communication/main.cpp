#include "mbed.h"

Serial pc(USBTX, USBRX); // pc tx, rx
Serial openmv(p9, p10);  // openmv tx, rx

int main() {
    pc.baud(115200);
    openmv.baud(115200);
    while(1) {
        pc.putc(openmv.getc());
    }
}
