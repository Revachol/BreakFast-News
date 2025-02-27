/** @type {import('tailwindcss').Config} */
module.exports = { 
    content: ["./src/**/*.{js,jsx,ts,tsx}"], 
    theme: { 
        extend: { 
            colors: { 
                primaryGreen: "#4CAF50", // Зеленый 
                primaryBlack: "#000000", // Черный 
                primaryWhite: "#FFFFFF", // Белый 
            } 
        }, 
    }, 
    plugins: [], 
}
