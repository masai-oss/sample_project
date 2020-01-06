/* eslint-disable react/prop-types */
import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './NavBarPublic.module.css';

const NavBar = ({ location: { pathname } }) => {
  if (pathname.startsWith('/dash')) return null;
  return (
    <div className={styles.NavLinks}>
      <NavLink to='/' exact activeClassName={styles.Active}>
        Home
      </NavLink>
      <NavLink to='/login' activeClassName={styles.Active}>
        Login
      </NavLink>
      <NavLink to='/register' activeClassName={styles.Active}>
        Register
      </NavLink>
      <NavLink to='/about' activeClassName={styles.Active}>
        About
      </NavLink>
      <NavLink to='/contact' activeClassName={styles.Active}>
        Contact
      </NavLink>
    </div>
  );
};

export default NavBar;
