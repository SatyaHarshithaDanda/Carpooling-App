#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>

struct RideRequest {
    std::string username;
    std::string fromLocation;
    std::string toLocation;
    std::string assignedDriver;
    std::string carNumber;
};

int main() {
    // Set response headers
    std::cout << "Content-type: text/html\n\n";
    
    std::cout << "<html><body>";

    // Get form data from environment variables
    char *data = getenv("QUERY_STRING");
    std::string input(data);

    // Parse form data
    std::string username, from, to;
    size_t pos = input.find("username=");
    if (pos != std::string::npos) {
        username = input.substr(pos + 9);
        pos = username.find("&");
        if (pos != std::string::npos) {
            username = username.substr(0, pos);
        }
    }

    pos = input.find("from=");
    if (pos != std::string::npos) {
        from = input.substr(pos + 5);
        pos = from.find("&");
        if (pos != std::string::npos) {
            from = from.substr(0, pos);
        }
    }

    pos = input.find("to=");
    if (pos != std::string::npos) {
        to = input.substr(pos + 3);
    }

    // Generate random driver and car number
    std::vector<std::string> availableDrivers = {"Driver1", "Driver2", "Driver3"};
    std::vector<std::string> availableCarNumbers = {"ABC123", "DEF456", "GHI789"};
    
    std::srand(static_cast<unsigned>(std::time(nullptr)));
    int driverIndex = std::rand() % availableDrivers.size();
    int carNumberIndex = std::rand() % availableCarNumbers.size();

    // Display submitted information
    std::cout << "<h2>Ride request added successfully!</h2>";
    std::cout << "<p>User: " << username << "</p>";
    std::cout << "<p>From: " << from << "</p>";
    std::cout << "<p>To: " << to << "</p>";
    std::cout << "<p>Assigned Driver: " << availableDrivers[driverIndex] << "</p>";
    std::cout << "<p>Car Number: " << availableCarNumbers[carNumberIndex] << "</p>";

    std::cout << "</body></html>";

    return 0;
}
