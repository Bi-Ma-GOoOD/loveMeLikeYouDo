im1 = imread("mri_txt.tif");
J = imadjust(im1, stretchlim(im1), []);
L = histeq(im1);
figure(1);imshow(im1)
figure(2);imshow(J)
figure(3);imshow(L)

im2 = imread("monet_gray_xlc.jpg");
K = histeq(im2);
K = adapthisteq(K);
figure(4);
imshow(K)