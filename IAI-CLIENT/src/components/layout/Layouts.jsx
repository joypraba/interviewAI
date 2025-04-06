import React, { useState } from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

const Layout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="app-container d-flex">
      <Sidebar isOpen={sidebarOpen} toggleSidebar={toggleSidebar} />
      <div className="main-content flex-grow-1">
        <Navbar toggleSidebar={toggleSidebar} />
        <div className="content-wrapper p-3">
          {children}
        </div>
      </div>
    </div>
  );
};

export default Layout;
