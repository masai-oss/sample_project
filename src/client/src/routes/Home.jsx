import React from "react";
import styles from "./Home.module.css";

const Home = () => {
  return (
    <div className={styles.home}>
      <header className={styles.header}>
        <h1>Masai Open Source</h1>
        <img src="/images/logo.svg" className={styles.reactLogo} alt="logo" />
        <p>
          Edit <code>src/routes/Home.js</code> and save to reload.
        </p>
        <p>
          An Initiative By{" "}
          <a
            className={styles.link}
            href="https://www.masaischool.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Masai School
          </a>
        </p>
      </header>
    </div>
  );
};

export default Home;
