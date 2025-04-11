%% Train Part
train_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\';
imageFiles = dir(fullfile(train_file, '*.jpg')); % List all JPG files
numImages = numel(imageFiles);

feature_vector_train = [];

for i = 1:numImages
    % Construct the full file path
    imgPath = fullfile(train_file, imageFiles(i).name); 
    img = imread(imgPath); % Read the image using the full path

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);

    shadding_pattern = imgaussfilt(gray_image, 225);
    h = double(shadding_pattern);
    g = double(gray_image);
    f = g ./ h;

    levelOtsu = graythresh(f);
    % levelAdap = adaptthresh(f);
    % disp(level);
    BW = imbinarize(f, 0.99);
    BW = ~BW;

    % Use imfill for patch hole for post-processing
    BW_fill = imfill(BW, "holes");
    figure(1);
    subplot(5, 5, i);
    imshow(BW_fill);

    % Step 02: Feature Extraction
    STATS = regionprops(BW_fill, 'Perimeter', 'Circularity', 'Eccentricity', 'Solidity',...
        'EquivDiameter', 'Extent');

    feature_vector_train(i, 1) = STATS.Perimeter;
    feature_vector_train(i, 2) = STATS.Circularity;
    feature_vector_train(i, 3) = STATS.Eccentricity;
    feature_vector_train(i, 4) = STATS.Solidity;
    feature_vector_train(i, 5) = STATS.EquivDiameter;
    feature_vector_train(i, 6) = STATS.Extent;

end

%% Test Part
test_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\';
imageFiles_test = dir(fullfile(test_file, '*.jpg')); % List all JPG files
numImages = numel(imageFiles_test);

feature_vector_test = [];

for i = 1:numImages
    % Construct the full file path
    imgPath = fullfile(test_file, imageFiles_test(i).name); 
    img = imread(imgPath); % Read the image using the full path

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);

    shadding_pattern = imgaussfilt(gray_image, 600);
    h = double(shadding_pattern);
    g = double(gray_image);
    f = g ./ h;

    level = graythresh(f);
    % disp(level);
    BW = imbinarize(f, 0.99);
    BW = ~BW;
    % figure(2);
    % subplot(3, 5, i);
    % imshow(BW);

    % Use imfill for patch hole for post-processing
    BW_fill = imfill(BW, "holes");

    % Step 02: Feature Extraction
    STATS = regionprops(BW_fill, 'Perimeter', 'Circularity', 'Eccentricity', 'Solidity',...
        'EquivDiameter', 'Extent');

    feature_vector_test(i, 1) = STATS.Perimeter;
    feature_vector_test(i, 2) = STATS.Circularity;
    feature_vector_test(i, 3) = STATS.Eccentricity;
    feature_vector_test(i, 4) = STATS.Solidity;
    feature_vector_test(i, 5) = STATS.EquivDiameter;
    feature_vector_test(i, 6) = STATS.Extent;
    
end

%% Step03: Classification
% Normalize Training Features
feature_vector_train = normalize(feature_vector_train, 'zscore');

% Normalize Testing Features using the same method
feature_vector_test = normalize(feature_vector_test, 'zscore');

% 3.1 Train a multiclass ECOC model using the default options.
load('trainLabel.mat');
Mdl = fitcecoc(feature_vector_train,trainLabel);
% 3.2 Prediction
load('testLabel.mat');
predictedLabels = predict(Mdl,feature_vector_test);
table(testLabel(:),predictedLabels (:),'VariableNames',{'TrueLabels','PredictedLabels'})

% Confusion Matrix
figure(3)
cm = confusionchart(testLabel, predictedLabels);