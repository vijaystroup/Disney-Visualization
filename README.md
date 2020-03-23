# Table of Contents
- [Overview](#overview)
- [Movie Gross](#movie-gross)
- [Ride Waiting Time](#ride-waiting-time)
- [Best Park Route](#best-park-route)

## Overview
This project was intended for me to learn about data science.  
The module *disney_movies_gross* and made plots of the values of Disney's movie's genre and ratings.  
The module *disney_ride_wait* which plots the average wait times of certain rides.  
The module *disney_best_park_route* which asks for a users input, and outputs the rides and times they should go to a park of their choosing.

## Movie Gross

The Movie Gross module examined data that had a movie title with its associated genre, rating, and gross. With this, I was able to see which type of movies are best sellers for Disney.  
The data that Adventure movies and G rated movies are what makes Disney the most money.

[Movie Gross Report](https://github.com/VijayStroup/Disney-Visualization/blob/master/disney_movies_gross_reports/final_report.md)


## Ride Waiting Time

The Ride Waiting Time module examined data that had a ride with the datetime and wait time for that perticular ride.  With this data, many plots with different time intervals were created.

[Movie Gross Report](https://github.com/VijayStroup/Disney-Visualization/blob/master/disney_ride_wait_reports/final_report.md)

## Best Park Route

The Best Park Route module examined the same data as the **Ride Waiting Time** module dataset and with this, calculated the order and times in which a user should go on rides to  
minimize the overall waiting time in lines at Disney Parks.

It starts off with asking the user to input the Disney Park and month they want to visit, then calculates the order and times in which they would have the least waiting time.  If I were to expand on this project more, I would take into consideration all years data not just 2019, and take the mean of the waiting times to
calculate the best times to go.  Also, I would ask the user for a restrictive time interval they would want to visit the park rather than just taking into
consideration all the hours of the day.

### sample output:
>Magic Kingdom(1) | Hollywood Studios(2) | Animal Kingdom(3) | Disneyland(4) | Epcot(5)
>
>Which park would you like to visit?(1-5): 6
>
>Invalid input, try again.
>
>Magic Kingdom(1) | Hollywood Studios(2) | Animal Kingdom(3) | Disneyland(4) | Epcot(5)
>
>Which park would you like to visit?(1-5): 2
>
>Jan(1) | Feb(2) | March(3) | April(4) | May(5) | June(6) | July(7) | Aug(8) | Sep(9) | Oct(10) | Nov(11) | Dec(12)
>
>When would you like to visit park 3?(1-12): 2
>
>    Park #2 | Month #2
>
>    The best day of the month to visit is: 6
>
>    Below is the order and times of which to visit the rides in your park...
>
>    slinky dog: 2019-02-06 06:51:09
>
>    toy story mania: 2019-02-06 07:23:07
>
>    rock n rollercoaster: 2019-02-06 09:09:08
>
>    alien saucers: 2019-02-06 19:58:09
