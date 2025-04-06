import React, { useState, useMemo, useEffect } from "react";
import DataTable from "react-data-table-component";
import { FaEdit, FaEye } from "react-icons/fa";
import { Link } from "react-router-dom";
import {getCandidates} from "../../services/Candidate"

const columns = [
  {
    id: 1,
    name: "Name",
    selector: (row) => row.name,
    sortable: true,
    reorder: true,
  },
  {
    id: 2,
    name: "Email",
    selector: (row) => row.email,
    sortable: true,
    reorder: true,
  },
  {
    id: 3,
    name: "Phone",
    selector: (row) => row.phone,
    sortable: true,
    right: true,
    reorder: true,
  },
  {
    name: "Actions",
    cell: row => (
      <div className="d-flex gap-2">
        <button
          className="btn btn-sm btn-primary"
          onClick={() => handleView(row)}
          title="View"
        >
          <FaEye />
        </button>
      </div>
    ),
    ignoreRowClick: true,
    allowOverflow: true,
    button: true,
  },
];

const Candidate = () => {
  const [filterText, setFilterText] = useState("");
  const [resetPaginationToggle, setResetPaginationToggle] = React.useState(false);
  const [candidates, setCandidates] = useState([])
  
  const handleView = () => {

  }
  
  const handleAppliedCandidates = (row) => {
    console.log("View applied candidates for", row);
    // Redirect or show modal
  };

  useEffect(() => {
    const fetchCandidates = async () => {
      try {
        const candidateData = await getCandidates();
        if (candidateData?.data) {
          setCandidates(candidateData.data);
        }
        console.log(candidateData?.data);
      } catch (error) {
        console.error("Failed to fetch candidates", error);
      }
    };

    fetchCandidates();
  }, []);

  
  
  const filteredItems = candidates.filter(item => item.name && item.name.toLowerCase().includes(filterText.toLowerCase()));
  const subHeaderComponentMemo = React.useMemo(() => {
    const handleClear = () => {
      if (filterText) {
        setResetPaginationToggle(!resetPaginationToggle);
        setFilterText('');
      }
    };
    return <input
      type="text"
      placeholder="Search by title"
      className="form-control w-25"
      value={filterText}
      onChange={e => setFilterText(e.target.value)}
    />;
  }, [filterText, resetPaginationToggle]);

  return (
    <DataTable
      title="Candidates"
      columns={columns}
      data={filteredItems}
      defaultSortFieldId={1}
      pagination
      subHeader
      subHeaderComponent={subHeaderComponentMemo}
      selectableRows
    />
  )
}


export default Candidate;