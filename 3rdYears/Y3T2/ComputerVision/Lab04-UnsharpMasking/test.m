originalImage = imread('dark_rays.jpg');

% Blur the original image (adjust sigma as needed)
sigma = 2; % Adjust sigma for desired blur level
blurredOriginal = imgaussfilt(originalImage, sigma);

% Calculate the difference
difference = originalImage - blurredOriginal;

% Scale the difference (adjust scalingFactor for desired sharpness)
scalingFactor = 1.5; % Adjust scalingFactor for desired sharpness
scaledDifference = difference * scalingFactor;

% Add the scaled difference to the original
unsharpenedImage = originalImage + scaledDifference;

% Display or save the result
imshow(unsharpenedImage);
