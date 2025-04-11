% Load the blurred image
blurred = imread('blurr.jpg');

% Define the Point Spread Function (PSF)
psf = fspecial('motion', 15, 30); % Motion blur PSF (15 pixels, 30 degrees)

% Deblur using Wiener filter
restored = deconvwnr(blurred, psf, 0.01); % 0.01 is noise power estimate

% Show results
imshowpair(blurred, restored, 'montage');
title('Original Blurred Image (Left) and Restored Image (Right)');
