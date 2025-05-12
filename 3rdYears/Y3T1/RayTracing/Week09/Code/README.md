# RT-python-week09
Ray tracing course week 09

This repository is for 'Raytracing in Entertainment Industry' (01418283).
This course is set to be taught for undergrad students at Dept of Computer Science, Faculty of Science, Kasetsart University.
The codes were rewritten and modified from https://raytracing.github.io/books/RayTracingInOneWeekend.html.

**Prerequisites :**
1. C/C++ or python.
2. Object-Oriented Programming (OOP).
3. Linear algebra for undergrad students.


**Class assignment**

Note that to submit the rendered results, please use the following parameters.
- at least 100 samples per pixel.
- at least 5 max depth.
- resolution width = 480p.
- aspect ratio = 16:9.


1. Implement the uniform hemisphere sampling approach in random_cosine_hemisphere_on_z() in RT_utility.py.
2. Replace the scattering method with the cosine sampling on hemisphere to the following materials.
    - TextureColor()
    - All implemented BRDFs
3. The 'pixel_sample_square()' method in RT_camera.py implemented how we can do jittering of a pixel. Explain each following term in details.
    - What is the term '-0.5' is for ?
    - What are the terms 's_i' and 's_j' for ?
    - Why do we multiply 'self.one_over_sqrt_spp' ?
    * Note that you might get the big picture of 'render_jittered()' to clearly explain the above terms.


