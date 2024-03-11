#include <catch2/catch.hpp>
#include "../MrSnowman/code/player_show.h"

TEST_CASE("Player_show Methods", "[class]") {

    SECTION("getAllSnowballs returns a reference to the list of SnowballAmmo_show") {
        // Arrange
        const double x = 0.0;
        const double y = 0.0;
        Player_show ps(x, y);

        // Act
        QList<SnowballAmmo_show*>& snowballs = ps.getAllSnowballs();

        // Assert
        REQUIRE(&snowballs == &ps.getAllSnowballs());
    }

}
