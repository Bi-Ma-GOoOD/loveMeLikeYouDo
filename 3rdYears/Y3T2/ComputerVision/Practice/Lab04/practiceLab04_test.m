% Read and display the image
I = imread('girl_gray.jpg');
imshow(I), title('Original Image');

% Add salt-and-pepper noise
noisyImage = imnoise(I, 'salt & pepper', 0.02);
figure, imshow(noisyImage), title('Image with Salt & Pepper Noise');

% Apply median filter for noise removal
medFiltered = medfilt2(noisyImage, [3 3]);
figure, imshow(medFiltered), title('Median Filtered Image');

% Add Gaussian noise
noisyGaussian = imnoise(I, 'gaussian', 0, 0.01);
figure, imshow(noisyGaussian), title('Image with Gaussian Noise');

% Create a Gaussian filter using fspecial and apply with imfilter
h = fspecial('gaussian', [5 5], 1); % 5x5 Gaussian filter with sigma=1
gaussFiltered = imfilter(noisyGaussian, h, 'symmetric');
figure, imshow(gaussFiltered), title('Gaussian Filtered Image');
