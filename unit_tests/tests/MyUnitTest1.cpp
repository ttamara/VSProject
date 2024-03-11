#include <catch2/catch.hpp>
#include "../MrSnowman/code/snowballammo_show.h"

TEST_CASE("SnowballAmmo_show", "[snowballammo_show]") {

    SECTION("SnowballAmmo_show - Check if setImg() does not cause any issues") {
        SnowballAmmo_show* snowballAmmoShow = new SnowballAmmo_show(0, 0, Direction::LEFT);
        snowballAmmoShow->setImg();
        // No specific requirements, just ensuring it doesn't crash
        delete snowballAmmoShow;
    }

    SECTION("SnowballAmmo_show - Check if animate() updates the position correctly") {
        SnowballAmmo_show* snowballAmmoShow = new SnowballAmmo_show(0, 0, Direction::LEFT);
        double initialX = snowballAmmoShow->x();
        snowballAmmoShow->animate();
        REQUIRE(snowballAmmoShow->x() != initialX);
        delete snowballAmmoShow;
    }

}
