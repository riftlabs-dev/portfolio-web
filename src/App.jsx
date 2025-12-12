import './App.css'
import PygameEmbed from './PygameEmbed';
import "@fontsource/inter/400.css";  // Regular weight
import "@fontsource/inter/500.css";  // Medium (optional)
import "@fontsource/inter/700.css";  // Bold (optional)   
import React, {useState } from 'react';

function App() {
  const [hoveredProject, setHoveredProject] = useState(null);

  // Define your design projects
  const designProjects = [
    { id: 1, name: "1 - Discovery Space Shuttle", image: "/space-shuttle-1.png", link: "/.html" },
    { id: 2, name: "2 - Hubble Space Telescope", image: "/hubble-4.png", link: "/.html" },
    { id: 3, name: "3 - Spitzner Space Telescope", image: "/spitzner-2.png",},
    { id: 4, name: "4 - Starship Enterprise NCC-1701", image: "/enterprise-1.png", },
    { id: 5, name: "5 - Utility Arm", image: "/arm-1.png"},
    { id: 6, name: "6 - R.Y.N.O", image: "/ryno-1.png"},
  ];
  return (
    <>
      <div class='container'>
        <div class="section-1 fade-in">
          <h1 style={{ whiteSpace: 'pre-line' }}>{'Software Development\n & Data Science'}</h1>
          <p style={{ whiteSpace: 'pre-line' }}>{'Freelance software developer and data analyst with +3 years exp. designing, building and testing full-stack custom applications. Specialise in rapid prototyping, data science and machine learning.\n\n Preferred stack: Python, React, SQL, C++, data science and machine learning libraries.\n'} </p>
          <div class="dropdown fade-in">
            <button class="dropbtn">Software & Data Science Projects</button>
            <div class="dropdown-content">
              <a href="https://cloud-chess.onrender.com/" target="_blank">1 - Cloud Chess</a>
              <a href="https://philosopher-bot-frontend.vercel.app/" target="_blank">2 - Philosophy Chatbot</a>
              <a href="https://portfolio-web-ten-chi.vercel.app/gll.html" target="_blank">3 - Landslide Locator / GIS</a>
              <a href="https://portfolio-web-ten-chi.vercel.app/project5.html" target="_blank">4 - River Toxicity</a>
            </div>
          </div>
        </div>
        {/* <div class="dropdown fade-in">
            <button class="dropbtn">Design & Manufacture Projects</button>
            <div class="dropdown-content">
              <a href="/.html" target="_blank">1 - Hubble Space Telescope</a>
              <a href="https://" target="_blank">2 - Spitzner Space Telescope</a>
              <a href="/pygbag/index.html" target="_blank">3 - Starship Enterprise NCC-1701</a>
              <a href="/.html" target="_blank">4 - Mechanical Arm</a>
              <a href="/.html" target="_blank">5 - R.Y.N.O</a>
            </div>
          </div> */}
        <div className="section-1 fade-in">
          <h1>Design & Manufacture</h1>
          <p style={{ whiteSpace: 'pre-line' }}>{'Novice designer with +2 years exp. in rapid prototyping and manufacture of custom parts and products using 3D printing. Materials used for production include PLA, TPU and PETG.\n\nSoftware used for model preparation includes Autodesk Fusion 360 / AutoCAD and Blender.'}</p>

          <div className="dropdown fade-in">
            <button className="dropbtn">Design & Manufacture Projects</button>
            <div className="dropdown-content">
              {designProjects.map((project) => (
                <a
                  key={project.id}
                  href={project.link}
                  target="_blank"
                  onMouseEnter={() => setHoveredProject(project)}
                  onMouseLeave={() => setHoveredProject(project)}
                >
                  {project.name}
                </a>
              ))}
            </div>
          </div>
              
          {/* Image Preview */}
          {hoveredProject && (
            <div className="image-preview">
              <img
                src={hoveredProject.image}
                alt="Project preview"
              />
            </div>
          )}
        </div>
        
        
        <div class="section-1 fade-in">
          <h1>Game Development</h1>
          <p style={{ whiteSpace: 'pre-line' }}>{'Indie game developer with +2 years exp. developing small cross-platform games using Python, C++ and Unreal Engine.'}</p>
          <div class="dropdown fade-in">
            <button class="dropbtn">Game Projects</button>
            <div class="dropdown-content">
              <a href="/pygbag/index.html" target="_blank">1 - Space Shooter</a>
            </div>
          </div>
        </div>
        <div>
          {/* <h2>Software and Data Projects</h2> */}
          {/* <img src="/gif-1.gif" alt="Portfolio" class="fade-in"style={{ borderRadius: '8px', width: '100%', maxWidth: '320px' }} />
           */}
        </div>
      </div>
    </>  
  )
}

export default App

