#include <fstream>
#include <iostream>

int main() {
    std::ofstream output("/tmp/safety_controller.log", std::ios::app);
    output << "controller-started" << std::endl;
    std::cout << "controller-started" << std::endl;
    return 0;
}
