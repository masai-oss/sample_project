/* eslint-disable react/prop-types */
import React from "react";
import { Link } from "react-router-dom";
import styles from "./NavBarPublic.module.css";

const NavBar = ({ location: { pathname } }) => {
  if (pathname.startsWith("/dash")) return null;
  return (
    <div className={styles.navLinks}>
      <Link to="/">
        <img
          src="https://avatars1.githubusercontent.com/u/59170916?s=200&v=4"
          alt="masai open source logo"
          width="50px"
        />
      </Link>
      <Link to="/">Home</Link>
      <Link to="/login">Login</Link>
      <Link to="/register">Register</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
    </div>
  );
};

export default NavBar;
