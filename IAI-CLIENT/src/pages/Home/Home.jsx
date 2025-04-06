import React from "react";
import { FaUserTie, FaUser  } from "react-icons/fa";
import { Link } from "react-router-dom";

function Home() {
  return <>
  {/* Warm Themed Centered Card */}
  <div
    className="d-flex justify-content-center align-items-center"
    style={{
      height: "100vh",
      background: "linear-gradient(to right, #FFD194, #D1913C)",
    }}
  >
    <div
      className="p-5 shadow-lg"
      style={{
        backgroundColor: "#fff5e6",
        borderRadius: "20px",
        maxWidth: "450px",
        width: "90%",
        textAlign: "center",
      }}
    >
      <h2
        className="mb-4"
        style={{ color: "#a0522d", fontWeight: "700", fontSize: "28px" }}
      >
        Welcome! Who Are You?
      </h2>

      <div className="d-flex flex-column gap-3">
        <Link to="/admin?role=1" className="text-decoration-none">
          <button
            className="btn btn-lg d-flex align-items-center justify-content-center w-100"
            style={{
              background: "linear-gradient(to right, #f2994a, #f2c94c)",
              color: "#fff",
              fontWeight: "600",
              border: "none",
              borderRadius: "12px",
              padding: "12px",
            }}
          >
            <FaUserTie className="me-2" /> Recruiter
          </button>
        </Link>

        <Link to="/candidate?role=2" className="text-decoration-none">
          <button
            className="btn btn-lg d-flex align-items-center justify-content-center w-100"
            style={{
              background: "linear-gradient(to right, #ff7e5f, #feb47b)",
              color: "#fff",
              fontWeight: "600",
              border: "none",
              borderRadius: "12px",
              padding: "12px",
            }}
          >
            <FaUser className="me-2" /> Candidate
          </button>
        </Link>
      </div>
    </div>
  </div>
</>

}

export default Home;