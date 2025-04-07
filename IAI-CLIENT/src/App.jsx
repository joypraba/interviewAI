import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from './pages/Dashboard/Dashboard';
import SignIn from './pages/Auth/Admin/Sign In/SignIn';
import SignUp from './pages/Auth/Admin/Sign Up/SignUp';
import JobListing from './pages/JobPosting/JobListing';
import Layout from './components/layout/Layouts';
import AddJobs from './pages/JobPosting/AddJobs';
import Candidate from './pages/Candidate/Candidate';
import Application from './pages/Application/Application';
import Job from './pages/Job/job';
import AppliedJob from './pages/AppliedJob/AppliedJob';
import Home from './pages/Home/Home';
import useTokenValidation from "./hooks/useTokenValidation";

function App() {
  useTokenValidation();
  return (
    <>
        <Routes>
        <Route path="/" element={<Home />} />
          <Route path="/admin" element={<SignIn />} />
          <Route path="/admin/sign-up" element={<SignUp />} />
          <Route path="/candidate" element={<SignIn />} />
          <Route path="/candidate/sign-up" element={<SignUp />} />
          {/* <Route path="/admin" element={<Layout />}> */}
            <Route path="/admin/jobs" element={<Layout><JobListing /></Layout>} />
            <Route path="/admin/jobs/add" element={<Layout><AddJobs /></Layout>} />
            <Route path="/admin/candidates" element={<Layout><Candidate /></Layout>} />
            <Route path="/admin/applications" element={<Layout><Application /></Layout>} />
            <Route path="/admin/dashboard" element={<Layout><Dashboard /></Layout>} />

            <Route path="/candidate/dashboard" element={<Layout><Dashboard /></Layout>} />
            <Route path="/candidate/jobs" element={<Layout><Job /></Layout>} />
            <Route path="/candidate/appliedJobs" element={<Layout><AppliedJob /></Layout>} />
          {/* </Route> */}

        </Routes>
    </>
  )
}

export default App
