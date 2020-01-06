import React from "react";
import { Link } from "react-router-dom";

const Dashboard = () => {
  return (
    <div>
      DASHBOARD HOME
      <Link to="/dash/settings">Settings</Link>
    </div>
  );
};

export default Dashboard;
