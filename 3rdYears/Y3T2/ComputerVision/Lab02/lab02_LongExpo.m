cd ('6510451115\lab2-long exposure\')
total = double(zeros(size(imread('1.jpg'))));
for i = 1:50
    filename = [num2str(i),'.jpg'];
    im = imread(filename);
    im = double(im);
    total = total + im;
end
total = uint8(total / 50);
imshow(total)
