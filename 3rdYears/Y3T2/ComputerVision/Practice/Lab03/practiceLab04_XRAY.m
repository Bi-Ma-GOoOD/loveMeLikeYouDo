im = imread('mri_txt.tif');
lims = stretchlim(im);
j = imadjust(im, lims, []);
% disp(lims);
h = histeq(im);
figure("Name","ORIGINAL");imshow(im);
figure("Name","IMADJUST");imshow(j);
figure("Name","HISTEQ");imshow(h);