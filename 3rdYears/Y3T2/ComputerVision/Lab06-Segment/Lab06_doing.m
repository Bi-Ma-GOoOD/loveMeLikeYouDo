image = imread("lymphomalplzhang03_shade.jpg");
gray = rgb2gray(image);
level = graythresh(gray);
bw = imbinarize(gray, level);
not_bw = ~bw;
not_image = ~image;

sigma = 25;
Iflatfield = imflatfield(gray,sigma);
subplot(1, 2, 1);
imshow(Iflatfield);
title(['Flat-Field Corrected Image, \sigma = ',num2str(sigma)])
subplot(1, 2, 2);
imshow(gray);