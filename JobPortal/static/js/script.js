// const jobsData = [
//   {
//     id: 1,
//     title: "Senior Software Engineer",
//     company: "TechCorp",
//     location: "San Francisco, CA",
//     type: "full-time",
//     experience: "senior",
//     category: "technology",
//     salary: "$120k - $180k",
//     salaryRange: "100k+",
//     posted: "2 days ago",
//     description:
//       "We're looking for a senior software engineer to join our growing team. You'll work on cutting-edge projects using modern technologies.",
//     tags: ["JavaScript", "React", "Node.js", "Remote"],
//   },
//   {
//     id: 2,
//     title: "Product Manager",
//     company: "InnovateLab",
//     location: "New York, NY",
//     type: "full-time",
//     experience: "mid",
//     category: "marketing",
//     salary: "$90k - $130k",
//     salaryRange: "50k-100k",
//     posted: "1 day ago",
//     description:
//       "Join our product team to drive innovation and deliver exceptional user experiences. Lead cross-functional teams to success.",
//     tags: ["Product Strategy", "Agile", "Analytics"],
//   },
//   {
//     id: 3,
//     title: "UX/UI Designer",
//     company: "DesignStudio",
//     location: "Remote",
//     type: "contract",
//     experience: "mid",
//     category: "design",
//     salary: "$70k - $100k",
//     salaryRange: "50k-100k",
//     posted: "3 days ago",
//     description:
//       "Create beautiful and intuitive user interfaces for web and mobile applications. Work with a talented design team.",
//     tags: ["Figma", "Sketch", "Prototyping", "Remote"],
//   },
//   {
//     id: 4,
//     title: "Data Scientist",
//     company: "DataTech",
//     location: "Austin, TX",
//     type: "full-time",
//     experience: "senior",
//     category: "technology",
//     salary: "$110k - $160k",
//     salaryRange: "100k+",
//     posted: "1 week ago",
//     description:
//       "Analyze complex datasets and build machine learning models to drive business insights and decision-making.",
//     tags: ["Python", "Machine Learning", "SQL", "TensorFlow"],
//   },
//   {
//     id: 5,
//     title: "Marketing Specialist",
//     company: "GrowthCo",
//     location: "Chicago, IL",
//     type: "full-time",
//     experience: "entry",
//     category: "marketing",
//     salary: "$50k - $70k",
//     salaryRange: "50k-100k",
//     posted: "4 days ago",
//     description:
//       "Execute marketing campaigns across multiple channels. Great opportunity for someone starting their marketing career.",
//     tags: ["Digital Marketing", "Social Media", "Content Creation"],
//   },
//   {
//     id: 6,
//     title: "Financial Analyst",
//     company: "FinanceFirst",
//     location: "Boston, MA",
//     type: "full-time",
//     experience: "mid",
//     category: "finance",
//     salary: "$75k - $95k",
//     salaryRange: "50k-100k",
//     posted: "5 days ago",
//     description:
//       "Analyze financial data and create reports to support strategic business decisions. Work with senior leadership team.",
//     tags: ["Excel", "Financial Modeling", "Analysis"],
//   },
//   {
//     id: 7,
//     title: "Junior Developer",
//     company: "StartupHub",
//     location: "Remote",
//     type: "full-time",
//     experience: "entry",
//     category: "technology",
//     salary: "$45k - $65k",
//     salaryRange: "0-50k",
//     posted: "1 day ago",
//     description:
//       "Perfect opportunity for new graduates to start their tech career. Work with experienced mentors on exciting projects.",
//     tags: ["JavaScript", "HTML", "CSS", "Remote"],
//   },
//   {
//     id: 8,
//     title: "Sales Manager",
//     company: "SalesForce Pro",
//     location: "Miami, FL",
//     type: "full-time",
//     experience: "senior",
//     category: "sales",
//     salary: "$85k - $120k",
//     salaryRange: "50k-100k",
//     posted: "3 days ago",
//     description:
//       "Lead a dynamic sales team and drive revenue growth. Excellent opportunity for experienced sales professionals.",
//     tags: ["Team Leadership", "CRM", "B2B Sales"],
//   },
// ]

// let currentJobs = [...jobsData]
// let displayedJobs = 6
// let currentFilters = {
//   search: "",
//   jobType: [],
//   experience: [],
//   category: [],
//   salary: [],
// }

// // Initialize the page
// document.addEventListener("DOMContentLoaded", () => {
//   displayJobs()
//   setupEventListeners()
//   updateJobCount()
// })

// // Display jobs
// function displayJobs(jobs = currentJobs.slice(0, displayedJobs)) {
//   const jobsContainer = document.getElementById("jobsContainer")

//   if (jobs.length === 0) {
//     jobsContainer.innerHTML = `
//       <div style="text-align: center; padding: 4rem; color: #64748b;">
//         <i class="fas fa-search" style="font-size: 4rem; margin-bottom: 1.5rem; opacity: 0.3;"></i>
//         <h3 style="margin-bottom: 1rem; color: #1a1a1a;">No jobs found</h3>
//         <p>Try adjusting your search criteria or browse all categories.</p>
//       </div>
//     `
//     return
//   }

//   jobsContainer.innerHTML = jobs
//     .map(
//       (job) => `
        // <div class="job-card" data-job-id="${job.id}">
        //   <div class="job-header">
        //     <div class="job-info">
        //       <h3>${job.title}</h3>
        //       <div class="company-name">${job.company}</div>
        //       <div class="job-location">
        //         <i class="fas fa-map-marker-alt"></i>
        //         ${job.location}
        //       </div>
        //     </div>
        //     <div class="company-logo">
        //       ${job.company.charAt(0)}
        //     </div>
        //   </div>
        //   <div class="job-details">
        //     <div class="job-tags">
        //       ${job.tags
        //         .map(
        //           (tag) => `
        //           <span class="job-tag ${
        //             tag.toLowerCase().includes("remote") ? "remote" : job.type === "full-time" ? "full-time" : ""
        //           }">${tag}</span>
        //       `,
        //         )
        //         .join("")}
        //     </div>
        //     <div class="job-description">${job.description}</div>
        //   </div>
        //   <div class="job-footer">
        //     <div>
        //       <div class="job-salary">${job.salary}</div>
        //       <div class="job-posted">Posted ${job.posted}</div>
        //     </div>
        //     <button class="apply-btn" onclick="applyToJob(${job.id})">
        //       Apply Now
        //     </button>
        //   </div>
        // </div>
//       `,
//     )
//     .join("")
// }

// // Setup event listeners
// function setupEventListeners() {
//   // Jobs search functionality
//   const jobsSearch = document.getElementById("jobsSearch")
//   if (jobsSearch) {
//     jobsSearch.addEventListener("input", (e) => {
//       currentFilters.search = e.target.value.toLowerCase()
//       applyFilters()
//     })
//   }

//   // Hero search functionality
//   document.getElementById("jobSearch")?.addEventListener("keypress", (e) => {
//     if (e.key === "Enter") {
//       searchJobs()
//     }
//   })

//   document.getElementById("locationSearch")?.addEventListener("keypress", (e) => {
//     if (e.key === "Enter") {
//       searchJobs()
//     }
//   })

//   // Mobile menu toggle
//   const hamburger = document.querySelector(".hamburger")
//   const navMenu = document.querySelector(".nav-menu")

//   if (hamburger) {
//     hamburger.addEventListener("click", () => {
//       navMenu.classList.toggle("active")
//     })
//   }

//   // Newsletter subscription
//   const newsletterForm = document.querySelector(".newsletter-form")
//   if (newsletterForm) {
//     newsletterForm.addEventListener("submit", function (e) {
//       e.preventDefault()
//       const email = this.querySelector('input[type="email"]').value
//       if (email) {
//         alert("Thank you for subscribing! You will receive job updates at " + email)
//         this.querySelector('input[type="email"]').value = ""
//       }
//     })
//   }
// }

// Apply filters
// function applyFilters() {
//   // Get selected filters
//   currentFilters.jobType = Array.from(
//     document.querySelectorAll(
//       'input[type="checkbox"][value="full-time"], input[type="checkbox"][value="part-time"], input[type="checkbox"][value="contract"], input[type="checkbox"][value="remote"]',
//     ),
//   )
//     .filter((cb) => cb.checked)
//     .map((cb) => cb.value)

//   currentFilters.experience = Array.from(
//     document.querySelectorAll(
//       'input[type="checkbox"][value="entry"], input[type="checkbox"][value="mid"], input[type="checkbox"][value="senior"]',
//     ),
//   )
//     .filter((cb) => cb.checked)
//     .map((cb) => cb.value)

//   currentFilters.category = Array.from(
//     document.querySelectorAll(
//       'input[type="checkbox"][value="technology"], input[type="checkbox"][value="marketing"], input[type="checkbox"][value="finance"], input[type="checkbox"][value="healthcare"], input[type="checkbox"][value="design"], input[type="checkbox"][value="sales"]',
//     ),
//   )
//     .filter((cb) => cb.checked)
//     .map((cb) => cb.value)

//   currentFilters.salary = Array.from(
//     document.querySelectorAll(
//       'input[type="checkbox"][value="0-50k"], input[type="checkbox"][value="50k-100k"], input[type="checkbox"][value="100k+"]',
//     ),
//   )
//     .filter((cb) => cb.checked)
//     .map((cb) => cb.value)

//   // Filter jobs
//   const filteredJobs = jobsData.filter((job) => {
//     // Search filter
//     const matchesSearch =
//       !currentFilters.search ||
//       job.title.toLowerCase().includes(currentFilters.search) ||
//       job.company.toLowerCase().includes(currentFilters.search) ||
//       job.tags.some((tag) => tag.toLowerCase().includes(currentFilters.search))

//     // Job type filter
//     const matchesJobType =
//       currentFilters.jobType.length === 0 ||
//       currentFilters.jobType.includes(job.type) ||
//       (currentFilters.jobType.includes("remote") && job.location.toLowerCase().includes("remote"))

//     // Experience filter
//     const matchesExperience =
//       currentFilters.experience.length === 0 || currentFilters.experience.includes(job.experience)

//     // Category filter
//     const matchesCategory = currentFilters.category.length === 0 || currentFilters.category.includes(job.category)

//     // Salary filter
//     const matchesSalary = currentFilters.salary.length === 0 || currentFilters.salary.includes(job.salaryRange)

//     return matchesSearch && matchesJobType && matchesExperience && matchesCategory && matchesSalary
//   })

//   currentJobs = filteredJobs
//   displayedJobs = Math.min(filteredJobs.length, 6)
//   displayJobs()
//   updateJobCount()

//   // Show/hide load more button
//   const loadMoreSection = document.getElementById("loadMoreSection")
//   if (displayedJobs >= currentJobs.length) {
//     loadMoreSection.style.display = "none"
//   } else {
//     loadMoreSection.style.display = "block"
//   }
// }

// Clear all filters
// function clearAllFilters() {
//   // Uncheck all checkboxes
//   document.querySelectorAll('.filter-checkbox input[type="checkbox"]').forEach((cb) => {
//     cb.checked = false
//   })

//   // Clear search
//   const jobsSearch = document.getElementById("jobsSearch")
//   if (jobsSearch) {
//     jobsSearch.value = ""
//   }

//   // Reset filters
//   currentFilters = {
//     search: "",
//     jobType: [],
//     experience: [],
//     category: [],
//     salary: [],
//   }

//   // Reset jobs
//   currentJobs = [...jobsData]
//   displayedJobs = 6
//   displayJobs()
//   updateJobCount()

//   // Show load more button
//   document.getElementById("loadMoreSection").style.display = "block"
// }

// // Update job count
// function updateJobCount() {
//   const jobCountElement = document.getElementById("jobCount")
//   if (jobCountElement) {
//     jobCountElement.textContent = currentJobs.length
//   }
// }

// // Sort jobs
// function sortJobs() {
//   const sortBy = document.getElementById("sortBy").value

//   switch (sortBy) {
//     case "newest":
//       currentJobs.sort((a, b) => new Date(b.posted) - new Date(a.posted))
//       break
//     case "oldest":
//       currentJobs.sort((a, b) => new Date(a.posted) - new Date(b.posted))
//       break
//     case "salary-high":
//       currentJobs.sort((a, b) => {
//         const aMax = Number.parseInt(a.salary.match(/\$(\d+)k/g)?.[1] || "0")
//         const bMax = Number.parseInt(b.salary.match(/\$(\d+)k/g)?.[1] || "0")
//         return bMax - aMax
//       })
//       break
//     case "salary-low":
//       currentJobs.sort((a, b) => {
//         const aMin = Number.parseInt(a.salary.match(/\$(\d+)k/)?.[1] || "0")
//         const bMin = Number.parseInt(b.salary.match(/\$(\d+)k/)?.[1] || "0")
//         return aMin - bMin
//       })
//       break
//   }

//   displayJobs()
// }

// Hero search functionality
// function searchJobs() {
//   const jobQuery = document.getElementById("jobSearch").value.toLowerCase()
//   const locationQuery = document.getElementById("locationSearch").value.toLowerCase()

//   const filteredJobs = jobsData.filter((job) => {
//     const matchesJob =
//       !jobQuery ||
//       job.title.toLowerCase().includes(jobQuery) ||
//       job.company.toLowerCase().includes(jobQuery) ||
//       job.tags.some((tag) => tag.toLowerCase().includes(jobQuery))

//     const matchesLocation = !locationQuery || job.location.toLowerCase().includes(locationQuery)

//     return matchesJob && matchesLocation
//   })

//   currentJobs = filteredJobs
//   displayedJobs = Math.min(filteredJobs.length, 6)
//   displayJobs()
//   updateJobCount()

//   // Scroll to results
//   document.getElementById("jobs").scrollIntoView({ behavior: "smooth" })
// }

// // Quick search functionality
// function quickSearch(query) {
//   document.getElementById("jobSearch").value = query
//   searchJobs()
// }

// // Load more jobs
// function loadMoreJobs() {
//   displayedJobs = Math.min(displayedJobs + 6, currentJobs.length)
//   displayJobs()

//   // Hide button if all jobs are displayed
//   if (displayedJobs >= currentJobs.length) {
//     document.getElementById("loadMoreSection").style.display = "none"
//   }
// }

// // Apply to job
// function applyToJob(jobId) {
//   const job = jobsData.find((j) => j.id === jobId)
//   alert(`Thank you for your interest in the ${job.title} position at ${job.company}! 
    
// In a real application, this would redirect you to the application form or the company's career page.`)
// }

// // Smooth scrolling for navigation links
// document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
//   anchor.addEventListener("click", function (e) {
//     e.preventDefault()
//     const target = document.querySelector(this.getAttribute("href"))
//     if (target) {
//       target.scrollIntoView({
//         behavior: "smooth",
//         block: "start",
//       })
//     }
//   })
// })

// Add scroll effect to header
// window.addEventListener("scroll", () => {
//   const header = document.querySelector(".header")
//   if (window.scrollY > 100) {
//     header.style.background = "rgba(255, 255, 255, 0.95)"
//     header.style.backdropFilter = "blur(20px)"
//   } else {
//     header.style.background = "rgba(255, 255, 255, 0.95)"
//     header.style.backdropFilter = "blur(20px)"
//   }
// })
