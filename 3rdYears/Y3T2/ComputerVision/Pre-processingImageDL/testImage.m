im = imread('Opisthorchis viverrine_0001.jpg');

im = im2double(im);

% Resize the image to 640x640 pixels
im = imresize(im, [640 640]);

b1 = medfilt2(im(:, :, 1), [13, 13]);
b2 = medfilt2(im(:, :, 2), [13, 13]);
b3 = medfilt2(im(:, :, 3), [13, 13]);
blur_image = cat(3, b1, b2, b3);
edge_image = im - blur_image;
% 4.5 for medfilt2
output_image = im + (2.0 * edge_image); 

subplot(1, 2, 1);
imshow(output_image);
subplot(1, 2, 2);
imshow(im);