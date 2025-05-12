im = imread('monet_gray_xlc.jpg');
h = histeq(im);
j = adapthisteq(im);
k = adapthisteq(h);
s = imadjust(h, stretchlim(h), []);
figure('Name','Histeq');imshow(h);
figure('Name', 'Adapthisteq');imshow(j);
figure('Name', 'Histeq -> Adapthisteq');imshow(k);
figure('Name','Imadjust');imshow(s);
% Show results
% imshowpair(h, k, 'montage');
% title('Histeq Image (Left) and Histeq -> Adapthisteq Image (Right)');