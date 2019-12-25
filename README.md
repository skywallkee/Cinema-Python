# Cinema Python

![Main Screen Of Application](https://i.imgur.com/me9YkI7.png)

Application implemented in Python that simulates a cinema. The application is able to:
- Add a movie
- Modify a movie
- Delete a movie (and delete all reservations made for the movie)
- Add a client fidelity card
- Modify a client card
- Delete a client card (and delete all reservations made with the card)
- Add a reservation for a movie by a card
- Modify a reservation
- Delete a reservation (and remove the points from the card)
- Search for a movie by a keyword
- Search for a client card by a keyword
- Display all the movies that are displayed in a timeframe
- Display all the movies descending by the number of reservations
- Display all the client cards descending by the number of points
- Remove all the reservations made in a timeframe
- Increase the points of all clients that have the birthday in a given year
- Undo actions did in the current session
- The deletion is not made permanently, objects are marked as deleted only and not actually erased
- The deletion is made in cascade (client -> reservations, movie -> reservations, reservations -> client points)
