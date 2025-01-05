im = imread('dark_rays.jpg');

%1
subplot(1, 3, 1);
imshow(im);
title('Original');

%2
b1 = medfilt2(im(:, :, 1), [11, 11]);
b2 = medfilt2(im(:, :, 2), [11, 11]);
b3 = medfilt2(im(:, :, 3), [11, 11]);
blur_image = cat(3, b1, b2, b3);
edge_image = im - blur_image;
% 4.5 for medfilt2
output_image = im + (2.5 * edge_image); 
% o1 = medfilt2(output_image(:, :, 1), [4, 4]);
% o2 = medfilt2(output_image(:, :, 2), [4, 4]);
% o3 = medfilt2(output_image(:, :, 3), [4, 4]);
% out = cat(3, o1, o2, o3);
out = imboxfilt(output_image, 3);
subplot(1, 3, 2);
imshow(out);
title('Unsharp - imboxfilt');

%3
b1 = medfilt2(im(:, :, 1), [11, 11]);
b2 = medfilt2(im(:, :, 2), [11, 11]);
b3 = medfilt2(im(:, :, 3), [11, 11]);
blur_image = cat(3, b1, b2, b3);
edge_image = im - blur_image;
% 4.5 for medfilt2
output_image = original + (4.7 * edge_image); 
o1 = medfilt2(output_image(:, :, 1), [4, 4]);
o2 = medfilt2(output_image(:, :, 2), [4, 4]);
o3 = medfilt2(output_image(:, :, 3), [4, 4]);
out = cat(3, o1, o2, o3);
subplot(1, 3, 3);
imshow(out);
title('Unsharp - medfilt2');