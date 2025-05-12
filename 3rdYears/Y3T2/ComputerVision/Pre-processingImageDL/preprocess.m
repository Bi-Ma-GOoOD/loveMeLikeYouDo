imageFolder = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Pre-processingImageDL\data_train_op\';
outputFolder = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Pre-processingImageDL\op_preprocessed';
imageFiles = dir(fullfile(imageFolder, '*.jpg'));
numImage = numel(imageFiles);

for i = 1:numImage
    img_get = imread(fullfile(imageFolder, imageFiles(i).name));

    % Convert to double precision for processing
    im = im2double(img_get);
    
    b1 = medfilt2(im(:, :, 1), [13, 13]);
    b2 = medfilt2(im(:, :, 2), [13, 13]);
    b3 = medfilt2(im(:, :, 3), [13, 13]);
    blur_image = cat(3, b1, b2, b3);
    edge_image = im - blur_image;
   
    output_image = im + (2.0 * edge_image); 
    
    % Save the processed image
    outputFile = fullfile(outputFolder, imageFiles(i).name);
    imwrite(output_image, outputFile);
end