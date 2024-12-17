original = imread('dark_rays.jpg');
im = rgb2gray(original);
j = imadjust(im, stretchlim(im), [0.0, 1.0]);

%Original
subplot(1, 3, 1);
imshow(original);
title('Original');

%1
img_blur = imgaussfilt(im, 3);
img_unsharp = original - img_blur;
img_output = original + (5 * img_unsharp);
img_output = imgaussfilt(img_output, 1.0);
subplot(1, 3, 2);
imshow(img_output);
title('Two');

%2
img_blur1 = imgaussfilt(j, 2);
img_unsharp1 = original - img_blur1;
img_output2 = original + (3 * img_unsharp1);
subplot(1, 3, 3);
imshow(img_output2);
title('Three');

