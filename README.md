# Pie-Site-Baker: A Deliciously Simple Static Site Generator

Pie-Site-Baker is a Python-based static site generator that makes creating websites as easy as pie! Whether you're cooking up a personal blog, a portfolio, or a simple landing page, Pie-Site-Baker has got you covered with its simple yet powerful recipe for baking perfect websites.

## Features

- Bake static HTML pages from Markdown content
- Serve up a tasty blog with customizable post metadata
- Dish out a professional resume page from JSON data
- Flexible templates using Jinja2 (our special pie crust!)
- Code syntax highlighting for the cherry on top
- Responsive design using Bootstrap (works on all plate sizes!)
- Light/Dark mode toggle (for day and night snacking)
- Easy configuration using YAML (our secret ingredient list)

## Installation

1. Preheat your oven (clone the repository):
   ```
   git clone https://github.com/yourusername/pie-site-baker.git
   cd pie-site-baker
   ```

2. Prepare your baking environment:
   ```
   conda create -n pie-site-baker python=3.8
   conda activate pie-site-baker
   ```

3. Mix in the required ingredients:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Customize your `config/config.yaml` file. This is your main recipe card:

   ```yaml
   site_name: "My Delicious Site"
   author: "Chef Extraordinaire"
   style:
     theme: light
     accent_color: '#FF6B6B'
     font: 'Georgia, serif'
   social_media:
     github: "https://github.com/chefextraordinaire"
     twitter: "https://twitter.com/chefextraordinaire"
   navigation:
     - name: Home
       url: index.html
     - name: Blog
       url: blog/index.html
     - name: Resume
       url: resume.html
   ```

2. Add your content:
   - Place Markdown files for blog posts in the `content/blog/` directory.
   - Edit `content/index.md` for your landing page.
   - Update `content/resume.json` with your resume information.

3. Customize the templates in the `templates/` directory if desired.

4. Bake your site:
   ```
   python main.py
   ```

5. Your freshly baked site will be in the `output/` directory, ready to serve!

## Customizing Your Pie

### Blog Posts and Landing Page

Use front matter at the top of your Markdown files to add metadata:

```markdown
---
title: "My First Blog Post"
date: 2023-08-10
author: "Chef Extraordinaire"
tags: ["baking", "websites"]
---

Here's the content of your post...
```

### Resume

The `resume.json` file follows the JSON Resume schema. Here's a taste:

```json
{
  "basics": {
    "name": "Chef Extraordinaire",
    "label": "Web Development Baker",
    "email": "chef@example.com",
    "phone": "(912) 555-4321",
    "url": "https://chefextraordinaire.com",
    "summary": "I bake websites that look good and taste even better.",
    "location": {
      "city": "San Francisco",
      "countryCode": "US",
      "region": "California"
    }
  },
  "work": [
    {
      "company": "Pie in the Sky Websites",
      "position": "Senior Baker",
      "startDate": "2020-01-01",
      "endDate": "Present",
      "summary": "Baking responsive, delicious websites",
      "highlights": [
        "Increased website flavor by 50%",
        "Reduced loading calories by 30%"
      ]
    }
  ],
  // ... more sections for education, skills, etc.
}
```

## Contributing

Got a tasty idea to improve Pie-Site-Baker? We'd love to have you in our kitchen! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use this recipe to bake your own delicious sites!