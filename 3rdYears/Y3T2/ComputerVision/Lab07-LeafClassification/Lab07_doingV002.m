clc; clear; close all;

% Train Part
train_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\';
imageFiles = dir(fullfile(train_file, '*.jpg')); % List all JPG files
numImages = numel(imageFiles);

% Initialize feature vector
feature_vector_train = zeros(numImages, 6); % 6 features: [Area, Perimeter, Circularity, Eccentricity, Aspect Ratio, Solidity]

for i = 1:numImages
    % Construct the full file path
    imgPath = fullfile(train_file, imageFiles(i).name); 
    img = imread(imgPath); % Read the image

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);
    
    % Remove shading using Gaussian filtering
    shadding_pattern = imgaussfilt(gray_image, 225);
    normalized_img = double(gray_image) ./ double(shadding_pattern);
    
    % Binarization using Otsu’s threshold
    BW = imbinarize(normalized_img, 0.99);
    BW = ~BW; % Invert the image (assuming leaf is dark on a light background)
    
    % Fill holes
    BW_fill = imfill(BW, 'holes');
    
    % Display images
    figure(1);
    subplot(5, 5, i);
    imshow(BW_fill);
    
    % Step 02: Feature Extraction
    stats = regionprops(BW_fill, 'Area', 'Perimeter', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Solidity');

    % Ensure at least one region is detected
    if ~isempty(stats)
        area = stats(1).Area;
        perimeter = stats(1).Perimeter;
        circularity = (4 * pi * area) / (perimeter^2);
        eccentricity = stats(1).Eccentricity;
        aspect_ratio = stats(1).MajorAxisLength / stats(1).MinorAxisLength;
        solidity = stats(1).Solidity;
    else
        % Default values if no leaf is detected
        area = 0; perimeter = 0; circularity = 0;
        eccentricity = 0; aspect_ratio = 0; solidity = 0;
    end

    % Store features in the training matrix
    feature_vector_train(i, :) = [area, perimeter, circularity, eccentricity, aspect_ratio, solidity];
end

%% Test Part
test_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\';
imageFiles_test = dir(fullfile(test_file, '*.jpg')); % List all JPG files
numTestImages = numel(imageFiles_test);

% Initialize feature vector for testing
feature_vector_test = zeros(numTestImages, 6);

for i = 1:numTestImages
    % Construct the full file path
    imgPath = fullfile(test_file, imageFiles_test(i).name); 
    img = imread(imgPath); % Read the image

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);
    
    % Remove shading using Gaussian filtering
    shadding_pattern = imgaussfilt(gray_image, 600);
    normalized_img = double(gray_image) ./ double(shadding_pattern);
    
    % Binarization using Otsu’s threshold
    BW = imbinarize(normalized_img, 0.99);
    BW = ~BW; % Invert the image

    % Fill holes
    BW_fill = imfill(BW, 'holes');

    % Display images
    figure(2);
    subplot(3, 5, i);
    imshow(BW_fill);

    % Step 02: Feature Extraction
    stats = regionprops(BW_fill, 'Area', 'Perimeter', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Solidity');

    % Ensure at least one region is detected
    if ~isempty(stats)
        area = stats(1).Area;
        perimeter = stats(1).Perimeter;
        circularity = (4 * pi * area) / (perimeter^2);
        eccentricity = stats(1).Eccentricity;
        aspect_ratio = stats(1).MajorAxisLength / stats(1).MinorAxisLength;
        solidity = stats(1).Solidity;
    else
        % Default values if no leaf is detected
        area = 0; perimeter = 0; circularity = 0;
        eccentricity = 0; aspect_ratio = 0; solidity = 0;
    end

    % Store features in the testing matrix
    feature_vector_test(i, :) = [area, perimeter, circularity, eccentricity, aspect_ratio, solidity];
end

%% Step 03: Classification
% Normalize Training Features
feature_vector_train = normalize(feature_vector_train, 'zscore');

% Normalize Testing Features using the same method
feature_vector_test = normalize(feature_vector_test, 'zscore');

% Load training labels
load('trainLabel.mat');

% Train a multiclass ECOC model using SVM
Mdl = fitcecoc(feature_vector_train, trainLabel);

% Load test labels
load('testLabel.mat');

% Predict test labels
predictedLabels = predict(Mdl, feature_vector_test);

% Display results
table(testLabel(:), predictedLabels(:), 'VariableNames', {'TrueLabels', 'PredictedLabels'})

% Confusion Matrix
figure(3)
confusionchart(testLabel, predictedLabels);

% Compute Accuracy
accuracy = sum(predictedLabels == testLabel) / length(testLabel) * 100;
fprintf('Model Accuracy: %.2f%%\n', accuracy);
