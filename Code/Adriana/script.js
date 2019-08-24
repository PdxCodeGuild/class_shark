//script.js

body {
  font-family: "open sans", sans-serif;
}

/* .navigation-menu class: Navigation wrapper
   .main-navigation class: Navigation links wrapper */

/* Mobile Version */

.navigation-menu {
  overflow: hidden;
  position: relative;
  border-bottom: 1px solid #e7e7e7;
}

/* Hiding the main navigation until it is clicked */

.main-navigation {
  display: none;
  padding-left: 0px;
}

.main-navigation li {
  list-style-type: none;
  margin: 15px auto;
  text-align: center;
}

.main-navigation a {
  padding: 5px 7px;
  color: #947aff;
  margin: 0px 2px 0px 2px;
  text-decoration: none;
  display: inline-block;
}

.main-navigation a:hover {
  color: black;
  transition: 0.3s ease;
}

.hamburger-icon {
  margin: 5px 30px 5px 5px;
  cursor: pointer;
  font-size: 25px;
  color: #947aff;
}

/* Hiding the checkbox */

#menu-toggle {
  display: none;
}

/* When the checkbox is ticked, the main navigation will display */

#menu-toggle:checked + .main-navigation {
  display: block;
}

/* Desktop Version */

@media screen and (min-width: 505px) {
  .navigation-menu {
    height: 70px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #e7e7e7;
  }

  .main-navigation {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    margin-left: 30px;
  }

  .main-navigation a {
    padding: 15px 17px;
  }

  /* Hiding the hamburger icon on larger screens */

  .hamburger-icon {
    display: none;
  }

  /* Ensuring that if the hamburger menu is active but
  the screen becomes larger, the display will
  change to display items in a row instead of a column*/

  #menu-toggle:checked + .main-navigation {
    display: flex;
  }
}
