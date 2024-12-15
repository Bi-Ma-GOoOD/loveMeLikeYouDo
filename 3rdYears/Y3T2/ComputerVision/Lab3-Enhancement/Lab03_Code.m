im  = imread('chest.jpg');
im = rgb2gray(im);
j = imadjust(im, [0.08, 0.51], [0.0, 1.0]);
k = histeq(im);
i = adapthisteq(im);

% show image of each figure
% figure('Name', 'ORIGINAL');imshow(im);
% figure('Name', 'IMADJUST');imshow(j);
% figure('Name', 'HISTEQ');imshow(k);
% figure('Name', 'ADAPTHISTEQ');imshow(i);

% try suplot 2 rows x 2 colomns
figure('Name', "Image Enhancement.");

subplot(2, 2, 1);
imshow(im);
title('ORIGINAL')

subplot(2, 2, 2);
imshow(j);
title('IMADJUST')

subplot(2, 2, 3);
imshow(k);
title('HISTEQ')

subplot(2, 2, 4);
imshow(i);
title('ADAPTHISTEQ')

